class GrammarFileMalformed(Exception):
    pass

def regex(reg, defs):
    """Return an hfst transducer with the specified replaced
    
    Args:
        reg (string): the regular expression to compile
        defs (
    """
class fst:
    def __init__(self):
        self.transducers = []
        
     = hfst.regex
    
    def clear(self):
        """Clears out the stack of transducers
        """
        self.transducers = []
        
    def compose(self, transducer):
        """Adds a new transducer on to the stack, this transducer is the composition of the
        last transducer on the stack and the transducer passed in
        
        Args:
            transducer (hfst.transducer): The transducer produced by a regex that will be composed
                                            and added to the top of the stack
        """
        top = self.transducers[-1].copy()
        top.compose(transducer)
        self.transducer.append(top)
        
    def sequence_walk(self, string):
        """Print what the string specified would look like after each stage of the composition
        
        Args:
            string: input string to pass through all the transducers
        """
        for transducer in transducers:
            print(transducer.lookup(string)))
            
    def compile_lexc_file(self, filepath:string):
        """Compiles a lexc file and adds the result to the last transducer in the stack
        
        Args:
            filepath (str): The path to the lexc file to read in
        """
        transducer = hfst.compile_lexc_file(filepath)
        if transducer == None:
            raise GrammarFileMalformed("The lexc file " + filepath + " could not be processed")
        else:
            self.transducers.append(transducer)
            
    def compile_sfst_file(self, filepath):
        """Compile an sfst file and adds the resulting fst at the top of the stack
        
        Args: 
            filepath (str): the path to the sfst rule file to process 
        """
        transducer = hfst.compile_sfst_file(filepath)
        if transducer == None:
            raise GrammarFileMalformed("The sfst file " + filepath + " could not be processed")
        else:
            self.transducers.append(transducer)
            
    def compile_twol_file(self, filepath):
        """Compile a two level morphology file and add the resulting fst to the top of the stack
        
        Args:
            filepath (str): the path to the twol file to process
        """
        transducer = hfst.compile_twol_file(filepath)
        if transducer == None:
            raise GrammarFileMalformed("The twol file " + filepath + " could not be processed")
        else:
            self.transducers.append(transducer)
            
    def remove_epsilons(self, string, epsilon='@_EPSILON_SYMBOL_@'):
        """Removes the epsilon transitions from the string along a path from hfst.

        Args:
            string (str): The string (e.g. input path, output form) from which the epsilons should be deleted.
            epsilon (str, optional):  The epsilon string to remove. Defaults to the default setting in hfst,
            '@_EPSILON_SYMBOL_@'. Pass this only if you've redefined the epsilon symbol string in hfst.

        Returns:
            str: The desired string, without epsilons

        """
        return string.replace('@_EPSILON_SYMBOL_@', '')


    def lookup(self, string):
        """Returns the output for an input in an hfst transducer, sans any epsilons or weights.
        
        Args:
            string (str): The string (input form) to be looked up in the HfstTransducer.

        Returns:
            str: The output of string in transducer
        """
        results = self.transducers[-1].lookup(string)
        if not results:
            raise FstPathNotFound("The string " + string + " was not found in the transducer")
        return [remove_epsilons(r[0]) for r in results]

    def test_fst(self, transducer, expected):
        """Tests whether an FST produces all output as provided in expected
        
        Args: 
            transducer (HfstTransducer): The HfstTransducer to use for testing
            expected (dict): This is a dictionary where the key is a word form and the 
                            value returned is a list of analyses for that key given the fst
        
        """
        error_count = 0
        pass_count = 0
        for key in expected:
            results = lookup(transducer, key)
            for item in results:
                if item not in expected[key]:
                    print("Your grammar output '" + item + "' given the input '" + key + "' instead of '" + expected[key] + "'")
                    error_count += 1

        error_percent = float(error_count) / len(expected.keys())
        print("There were " + str(error_count) + " errors")
        print("Your error percent is" + str(error_percent)) 
        if error_count == 0:
            print("PASSED!!!!")
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
            pairs += remove_epsilons(input) + ":\n"
            for output in outputs:
                out = remove_epsilons(output[0])
                pairs += " " + out + "\n"
        return pairs


    def read_test_file(filepath):
        """
        Read in the test file specified where each line is a target input to the 
        transducer. The left token is the input to the transducer and the right token
        is the output from the transducer.
        """
        expected_output = {}
        with open(filepath) as tst_file:
            for line in tst_file:
                line = line.split()
                line = [piece.strip() for piece in line]
                expected_output[line[0]] = line[1]
                
        return expected_output


class FstPathNotFound(Exception):
    pass


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
        for fstname, regex in self.defs.items():
            replaced = True
            while replaced:
                replaced = False
                for fstname2, regex2 in self.defs.items():
                    if fstname != fstname2:
                        result = regex.replace(fstname2, regex2)
                        if result != regex:
                            self.defs[fstname] = result
                            regex = result
                            replaced = True
                            break


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
