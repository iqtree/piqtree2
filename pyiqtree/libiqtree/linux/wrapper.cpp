extern "C" {
    int calculate_RF_distance(const char* tree1, const char* tree2);
    void generate_random_tree_file(int numtaxa, int seed, const char* gen_mode, const char* filename);
    void phylogenetic_analysis(const char* alignment_file, int ncpus);

    // Wrapper functions
    int calculate_RF_distance_wrapper(const char* tree1, const char* tree2) {
        return calculate_RF_distance(tree1, tree2);
    }

    void generate_random_tree_file_wrapper(int numtaxa, int seed, const char* gen_mode, const char* filename) {
        generate_random_tree_file(numtaxa, seed, gen_mode, filename);
    }

    void phylogenetic_analysis_wrapper(const char* alignment_file, int ncpus) {
        phylogenetic_analysis(alignment_file, ncpus);
    }
}
