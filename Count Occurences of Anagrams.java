class solution {
    int search(string n, string m) {
        if (n.length() > m.length()) {
            return 0;
        }
        int[] nf = new int[26];
        int[] mf = new int[26];
        int c = 0;
        for (int i = 0; i < p.length(); i++) {
            nf[n.charAt(i) - 'a']++;
            mf[m.charAt(i) - 'a']++;
        }
        if (Arrays.equals(nf, mf)) {
            c++;
        }
        for (int i = n.length(); i < m.length(); i++) {
            mf[m.charAt(i - n.length()) - 'a']--;
            mf[m.charAt(i) - 'a']++;
            if (Arrays.equals(nf, mf)) {
                c++;
            }
        }
        return c;
    }
}