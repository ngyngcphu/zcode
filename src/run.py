import os, subprocess, sys
import unittest

for path in ['./test/', '../target' './main/zcode/parser/', './main/zcode/utils/', './main/zcode/astgen/', './main/zcode/checker/', './main/zcode/codegen/']:
    sys.path.append(path)

ANTLR_JAR = os.environ.get('ANTLR_JAR')

def main(argv):
    if len(argv) not in [1, 2]:
        printUsage()
    
    elif argv[0] == 'gen':
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", '../target',
                        "-no-listener", "-visitor", "-Xexact-output-dir", "main/zcode/parser/ZCode.g4"])
    
    elif argv[0] == 'test':
        # if os.path.exists('./main/zcode2/parser'):
        #     subprocess.run(["java", "-jar", ANTLR_JAR, "-o", './main/zcode2/parser',
        #                 "-no-listener", "-visitor", "-Xexact-output-dir", "./main/zcode2/parser/ZCode.g4"])
        
        # else:
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", '../target',
                    "-no-listener", "-visitor", "-Xexact-output-dir", "main/zcode/parser/ZCode.g4"])
        
        if argv[1] in ['LexerSuite', 'ParserSuite', 'ASTGenSuite', 'ASTTest', 'CheckSuite', 'LexerSuite_VoTien', 'ParserSuite_VoTien', 'ASTGenSuite_TanNguyen']:
            exec(f'from {argv[1]} import {argv[1]}')
            exec(f'getAndTest({argv[1]})')

        else:
            printUsage()
    
    elif argv[0] == 'genTest':
        if argv[1] in ['LexerSuite', 'ParserSuite', 'ASTGenSuite']:
            subprocess.run(["python3", "genTestCase.py", argv[1]])
        
        else:
            printUsage()
    
    elif argv[0] == 'clean':
        files = ['ZCodeLexer.py', 'ZCodeParser.py', 'ZCodeLexer.tokens', 'ZCode.interp', 'ZCode.tokens', 'ZCodeLexer.interp', 'ZCodeVisitor.py']
        for file in files:
            if os.path.exists(f'./main/zcode/parser') and os.path.isfile(f'./main/zcode/parser/{file}'):
                os.remove(f'./main/zcode/parser/{file}')

            # if os.path.exists(f'./main/zcode2/parser') and os.path.isfile(f'./main/zcode2/parser/{file}'):
            #     os.remove(f'./main/zcode2/parser/{file}')
            
            if os.path.exists(f'../target') and os.path.isfile(f'../target/{file}'):
                os.remove(f'../target/{file}')

    else:
        printUsage()

def getAndTest(cls):
    from io import StringIO
    testLoader = unittest.TestLoader()
    suite = testLoader.loadTestsFromTestCase(cls)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    stream.seek(0)
    res = stream.read().split('\n')[0]
    for idx in range(result.testsRun):
        print(f"Testcase {idx + 1}: {'Passed' if res[idx] == '.' else 'Failed'}")
    
    print(f"Score: {res.count('.')}/{result.testsRun}")
    
def printUsage():
    print('python3 run.py clean') # Clean the generated file in target folder and ./main/zcode/parser folder
    print('python3 run.py gen')   # Remember to run this code before generating testcases
    print('python3 run.py test LexerSuite')
    print('python3 run.py test ParserSuite')
    print('python3 run.py test ASTGenSuite')
    print('python3 run.py test CheckSuite')
    print('python3 run.py genTest LexerSuite')
    print('python3 run.py genTest ParserSuite')
    print('python3 run.py genTest ASTGenSuite')

if __name__ == '__main__':
    main(sys.argv[1:])