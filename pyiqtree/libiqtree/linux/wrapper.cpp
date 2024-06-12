extern "C" {
    int calculate_RF_distance(const char* tree1, const char* tree2);
    void generate_random_tree_file(int numtaxa, int seed, const char* gen_mode, const char* filename);
    void phylogenetic_analysis(const char* alignment_file, int ncpus);
}
