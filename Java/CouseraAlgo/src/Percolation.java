import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private WeightedQuickUnionUF link;
    private boolean[] lst;
    private int num;
    private int openSites;

    // creates n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        link = new WeightedQuickUnionUF(n*n + 2);
        lst = new boolean[n*n];
        num = n;
        openSites = 0;

        for (int i = 0; i < n; i++) {
            // initiallizing lst {0,1}
            lst[i] = false;

            // linking imagery nodes to first and last rows
            link.union(n*n, i); // top imagery node
            link.union(n*n + 1, n*(n-1) + i); // bottom imagery node
        }
    }

    private int rowcolToNum(int row, int col) {
        return row*num + col;
    }

    // opens the site (row, col) if it is not open already
    public void open(int row, int col) {
        int curNum = rowcolToNum(row, col);
        if (isFull(row, col)) {
            // opening (row,col) in list with {0,1}
            lst[curNum] = true;
            openSites += 1;
            
            // linking (row,col) with opened sites on UDLR
            if ((curNum+1)/num == row && curNum+1 < num*num) if (lst[curNum+1] == true) link.union(curNum, curNum+1); // doesn't exceed the row && be less than N*N
            if ((curNum-1)/num == row && curNum-1 >= 0) if (lst[curNum-1] == true) link.union(curNum, curNum-1); // doesn't exceed the row && be >= 0
            if (curNum+num < num*num) if (lst[curNum+num] == true) link.union(curNum, curNum+num);
            if (curNum-num >= 0) if (lst[curNum-num] == true) link.union(curNum, curNum-num);
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        return lst[rowcolToNum(row, col)] == true;
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        return lst[rowcolToNum(row, col)] == false;
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return openSites;
    }

    // does the system percolate?
    public boolean percolates() {
        return link.find(num*num) == link.find(num*num+1);
    }

    // test client (optional)
    public static void main(String[] args) {

    }
}
