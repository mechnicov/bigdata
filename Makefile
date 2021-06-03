method := 'default'

task2_generate:
	cd task2 && ./gradlew generate
task2_calculate:
	cd task2 && ./gradlew calculate --args=$(method)
