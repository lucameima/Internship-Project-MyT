from quickumls import QuickUMLS
import pandas as pd

def itterating_sentences (path_to_directory_condition):
    """
    param: path to directory where list of varaibles is stored
    returns list of sentences
    """
    columns = []
    sentences = []
    with open(path_to_directory_condition, encoding='ISO-8859-1') as csv_file:
        for row in csv_file:
            row = row.strip('\n')
            column = row.split('\t')
            columns.append(column)
    for x in columns[1:]: # leaving out headers
        sentences.append(x[0])
    return sentences

def list_conditions_with_qumls(path_to_directory_condition, path_to_qumls_files):
    """
    param: path to directory where list of conditions is stored
    returns for each variable what part of the string is recognized as a biomedical concept, to which biomedical concept it is mapped, and if its fully/partly or not recognized,
    """

    term_dict =dict()
    matcher = QuickUMLS(path_to_qumls_files)
    for string in itterating_sentences (path_to_directory_condition):
        x = matcher.match(string, best_match=True, ignore_syntax=False)
        term_string=string
        if len(x) > 0:
            for y in x:
                for z in y:
                    ngram = z["ngram"]
                    term2 = z["term"]
                    term3 = z["similarity"]
                    if term_string.lower() == term2.lower():
                        term_dict[term_string] =[ngram, term2, "full recognition"]
                    if term_string.lower() != term2.lower():
                        term_dict[term_string] =[ngram, term2, "partial recognition", term3]

        if len(x) == 0:
            term_dict[term_string] = ["none","none","not recognized"]
    return term_dict

def counting_scores_of_recognition(path_to_directory_condition, path_to_qumls_files):
    """
    param1: path to directory where list of conditions is stored
    param2:  path to directory where the files of qumls are stored
    returns dictionary with for each condition if it is fully, partially or not recongized by QuickUMLS

    """
    score_dict = {}
    term_dict = list_conditions_with_qumls(path_to_directory_condition, path_to_qumls_files)
    df1 = pd.DataFrame.from_dict(term_dict, orient='index', columns = ["ngram", "concept", "score"])
    full_rec_counter = 0
    part_rec_counter = 0
    not_rec_counter = 0


    for row in df1.values:
        score = row[2]
        if score == 'full recognition':
            full_rec_counter +=1
        if score == 'partial recognition':
            part_rec_counter +=1
        if score == 'not recognized':
            not_rec_counter +=1
    score_dict["full recognition"] = full_rec_counter
    score_dict["partial recognition"] = part_rec_counter
    score_dict["no recognition"] = not_rec_counter

    return score_dict

def creating_reg_ex_list(path_to_directory_condition, path_to_dut_qumls_files,  path_to_eng_qumls_files):
    """
    param1: path to directory where list of conditions is stored
    param2:  path to directory where the  Dutch files of qumls are stored
    param3:  path to directory where the  English files of qumls are stored
    returns list with strings with words which are not recognized by either Dutch and English QuickUMLS
    """
    dictned = list_conditions_with_qumls(path_to_directory_condition, path_to_dut_qumls_files)
    dicteng = list_conditions_with_qumls(path_to_directory_condition, path_to_eng_qumls_files)
    compare_dict = {}
    reg_ex_list = []
    for (k,v), (k2,v2) in zip(dictned.items(), dicteng.items()):
        compare_dict[k] = v[1], v[2], v2[1], v2[2]
        if v2[2] == "not recognized" and v[2]=="not recognized":
            reg_ex_list.append(k)

    return reg_ex_list
