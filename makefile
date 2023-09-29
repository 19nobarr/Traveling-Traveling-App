clean:
	rm -f $(OBJECTS) $(EXECUTABLE) $(EXECUTABLE)_debug $(EXECUTABLE)_profile \
      $(TESTS) $(PARTIAL_SUBMITFILE) $(FULL_SUBMITFILE) $(PERF_FILE) \
      $(UNGRADED_SUBMITFILE)
	rm -Rf *.dSYM

make: 
	