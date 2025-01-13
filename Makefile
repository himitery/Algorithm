test:
	@$(MAKE) test_baekjoon

test_baekjoon:
	@for dir in baekjoon/python/*; do \
		if [ -d "$$dir" ]; then \
			pytest "$$dir"; \
		fi; \
	done