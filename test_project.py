from project import read_genes_from_file, find_matches, display_results

def test_read_genes_from_file():
    with open("genes.txt", "w") as f:
        f.write("GeneA: ATCG\n")
        f.write("GeneB: GGTT\n")
    gene = read_genes_from_file()
    if gene != {"GeneA": "ATCG", "GeneB": "GGTT"}:
        print("test_read_genes_from_file failed", gene)
    else:
        print("test_read_genes_from_file passed")

def test_find_matches():
    genes = {"Hereditary Breast & Ovarian Cancer Syndrome - BRCA1" : "CGCTGCTCCCTCTTTGCGAGAACTGCACTT",
             "Li-Fraumeni syndrome / multiple cancers - TP53" : "TCATACAGCCCCAAGCACGGCCCATGGGAT"}
    sequence = "CGCTGCTCCCTCTTTGCGAGAACTGCACTT"
    matches = find_matches(genes, sequence, threshold=0.85)
    if ("Hereditary Breast & Ovarian Cancer Syndrome - BRCA1", 100.0) not in matches:
        print("test_find_matches failed", matches)
    else:
        print("test_find_matches passed")

def test_display_results():
    result1 = display_results([])
    assert result1 == "No matching genes found.", "Unexpected output for no matches"
    result2 = display_results([("GeneX", 95.0)])
    if "GeneX (95.0%)" not in result2:
        print("test_display_results failed", result2)
    else:
        print("test_display_results passed")

if __name__ == "__main__":
    test_read_genes_from_file()
    test_find_matches()
    test_display_results()
