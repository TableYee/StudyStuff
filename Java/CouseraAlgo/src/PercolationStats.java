import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private Percolation pc;
    private double[] results;
    private double t;
    private double CONFIDENCE_95 = 1.96;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        results = new double[trials];
        t = Double.valueOf(trials);
        int randRow, randCol;

        for (int i = 0; i < trials; i++) {
            pc = new Percolation(n);

            while (true) {
                randRow = StdRandom.uniformInt(0, n);
                randCol = StdRandom.uniformInt(0, n);
                pc.open(randRow, randCol);

                if (pc.percolates()) {
                    results[i] = (double) pc.numberOfOpenSites()/(n*n);
                    break;
                }
            }
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(results);
    }

    // sample standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(results);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - (CONFIDENCE_95 * stddev())/Math.sqrt(t);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + (CONFIDENCE_95 * stddev())/Math.sqrt(t);
    }

   // test client (see below)
   public static void main(String[] args) {
        PercolationStats pcStats = new PercolationStats(200, 100);
        System.out.printf("%-30s = %f \n", "mean", pcStats.mean());
        System.out.printf("%-30s = %f \n", "stddev", pcStats.stddev());
        System.out.printf("%-30s = [%f, %f] \n", "95% confidence interval", pcStats.confidenceLo(), pcStats.confidenceHi());
        
   }
}