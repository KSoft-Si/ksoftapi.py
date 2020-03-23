import sys
from io import StringIO

import pylint.lint as pylint
from flake8.api import legacy
from pylint.reporters import text


def test_flake8():
    style_guide = legacy.get_style_guide()
    report = style_guide.check_files(['ksoftapi'])
    statistics = report.get_statistics('E')
    failed = bool(statistics)

    return failed


def test_pylint():
    stdout = StringIO()
    reporter = text.TextReporter(stdout)
    opts = ['--max-line-length=150', '--score=no', '--disable=missing-docstring, wildcard-import, '
                                                   'attribute-defined-outside-init, too-few-public-methods, '
                                                   'old-style-class,import-error,invalid-name,no-init,'
                                                   'too-many-instance-attributes,protected-access,too-many-arguments,'
                                                   'too-many-public-methods,logging-format-interpolation,'
                                                   'too-many-branches', 'ksoftapi']
    pylint.Run(opts, reporter=reporter, do_exit=False)
    out = reporter.out.getvalue()

    failed = bool(out)

    return failed


def test_import():
    try:
        import ksoftapi
    except:
        return True


if __name__ == '__main__':
    tests = [test_flake8, test_pylint, test_import]
    fail_count = 0

    for test in tests:
        test_name = test.__name__
        formatted_test_name = f'-- {test_name[5:]} test --'
        print(formatted_test_name)

        failed = test()
        if failed:
            print('Failed')
            fail_count += 1
        else:
            print('Passed')

    print(f'Fails: {fail_count}')
    if fail_count == 0:
        sys.exit(0)
    else:
        sys.exit(1)
