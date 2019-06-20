def remove_epsilons(string, epsilon='@_EPSILON_SYMBOL_@'):
    """Removes the epsilon transitions from the string along a path from hfst.

    Args:
        string (str): The string (e.g. input path, output form) from which the epsilons should be deleted.
        epsilon (str, optional):  The epsilon string to remove. Defaults to the default setting in hfst,
        '@_EPSILON_SYMBOL_@'. Pass this only if you've redefined the epsilon symbol string in hfst.

    Returns:
        str: The desired string, without epsilons

    """
    return string.replace('@_EPSILON_SYMBOL_@', '')


def lookup(transducer, string):
    """Returns the output for an input in an hfst transducer, sans any epsilons or weights.
    
     Args:
        transducer (HfstTransducer): the HfstTransducer in which lookup should be performed.
        string (str): The string (input form) to be looked up in the HfstTransducer.

    Returns:
        str: The output of string in transducer
    """
    try:
        result = transducer.lookup(string)
        result = remove_epsilons(transducer.lookup(string)[0][0])

    except IndexError:
        raise Exception("Word form " + string + " not found in transducer")

    return result

def test_fst(transducer, expected):
    """Tests whether an FST produces all output as provided in expected
    
    Args: 
        transducer (HfstTransducer): The HfstTransducer to use for testing
        expected (dict): This is a dictionary where the key is a word form and the 
                         value returned is a list of analyses for that key given the fst
    
    """
    error_count = 0
    pass_count = 0
    for key in expected:
        res = fst.lookup(key)
        for item in res:
            if not in expected[key]:
                print("Your grammar over generates the word " + item + " given the input " + key)
                error_count += 1

        for val in expected[key]:
            if val not in res:
                print("Your grammar does not generate the word " + val + " given the input " + key)
                error_count += 1

    print("There were " + str(error_count) + " errors")
    if error_count == 0:
        return True
    else:
        return False

def pairs(transducer):
    """Enumerates all possible input-output pairs in an hfst transducer. Best suited to be printed.
    
     Args:
        transducer (HfstTransducer): the HfstTransducer to enumerate.

    Returns:
        str: all possible input-output pairs in transducer, pretty printed
    """
    pairs = ''
    results = transducer.extract_paths(output='dict')
    for input,outputs in results.items():
        pairs += f'{remove_epsilons(input)}:\n'
        for output in outputs:
            out = remove_epsilons(output[0])
            pairs += f' {out}\n'
    return pairs


class Definitions:
    """A utility class for creating Set FSTs for reuse in FST regex.
    
    (Set FST, e.g., [a|i|u|e|o])
    
    For example, we might wish to replace V with all the vowels of our language in a regex. This
    is not possible natively with hfst, but we achieve it using string manipulations. Simply
    add your desired replacement sets and desired names to the constructor dictionary, then call
    the replace method of the resulting object on a regex string before passing it to hfst.
    """
    def __init__(self, definitions):
        """
        Args:
            definitions (dict): dictionary with keys of Fst set names, and values of regex sets.
        """
        self.defs = definitions

    def replace(self, string):
        """Replaces all defined set names occuring in regex string with corresponding set.
        
        Args:
            string (str): string in which we wish to replace defined FST names with corresponding FSTs.
        Returns:
            str: The original string with the defined FSTs substituted in place of their names.
        """
        for i, j in self.defs.items():
            string = string.replace(i, j)
        return string
