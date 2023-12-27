public class QuickUnionWeightedUF {
    private int[] id, sz;

    public QuickUnionWeightedUF(int N) {
        id = new int[N];
        sz = new int[N];

        for(int i = 0 ; i < N ; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }
    
    private int root(int i) {
        while(i != id[i]) {
            id[i] = id[id[i]]; // Path Compression
            i = id[i];
        } 
        return i;
    }

    private boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    private void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        
        // weighted
        if(sz[i] < sz[j]) {
            id[i] = j;
            sz[j] += sz[i];
        } else{
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}