all:
	@echo "Available targets:"
	@echo "  install     - Install dependencies"
	@echo "  test        - Run MD5 checksum tests"
	@echo "  result      - Save test results to result.txt"
	@echo "  merge       - Merge development into master"
	@echo "  development - Reset development branch to master"
	@echo "  tag         - Create and push tag (usage: make tag TAG=2026.04.17)"
	@echo "  clean       - Remove node_modules and result files"

node_modules:
	@npm install
	@touch node_modules

install: node_modules
	@echo "✅ Dependencies installed"

test: install
	@npm test && echo "✅ All tests passed" || (echo "❌ Tests failed"; exit 1)

result: install
	@npm test > result.txt 2>&1 && echo "✅ Results saved to result.txt"

# 重置 development 分支为 master（谨慎使用）
development:
	@echo "⚠️  Warning: This will reset development branch to match master"
	@read -p "Are you sure? (y/N) " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		git checkout development && \
		git reset --hard master && \
		git push --force-with-lease origin development && \
		echo "✅ Branch development reset to master"; \
	else \
		echo "❌ Cancelled"; \
	fi

# 合并 development 到 master
merge:
	@echo "Merging development into master..."
	@git checkout master && \
	git pull origin master && \
	git checkout development && \
	git pull origin development && \
	git checkout master && \
	git merge development && \
	git push origin master --tags && \
	echo "✅ Merge complete"

# 创建并推送 tag
tag:
	@if [ -z "$(TAG)" ]; then \
		echo "❌ Usage: make tag TAG=2026.04.17"; \
		exit 1; \
	fi
	@echo "Creating tag: $(TAG)"
	@git tag -a "$(TAG)" -m "Release version $(TAG)" && \
	git push origin "$(TAG)" && \
	echo "✅ Tag $(TAG) created and pushed"

# 清理
clean:
	@rm -rf node_modules/ result.txt
	@echo "✅ Cleaned"

.PHONY: all install test result development merge tag clean
