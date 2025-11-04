def fake_error_trace():
    print("Traceback (most recent call last):")
    print('  File "calc.py", line 666, in <module>')
    print("    perform_arithmetic()")
    print("  File \"calc.py\", line 13, in perform_arithmetic")
    print("    raise CorruptedRealityError('value mismatch')")
    print("CorruptedRealityError: value mismatch — recommended action: GIVE ME YOUR SOUL")
