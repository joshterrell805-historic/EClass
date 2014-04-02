# all .class files depend on .java files
# build each .java file into a .class file
bin/%.class: src/%.java;\
javac -d bin -cp "lib/jfxrt.jar" src/$*.java

#build all the class files and the jar file
build: copy_dependencies bin/application/*.class manifest.txt

# make sure everything is up to date then run the latest version of the program
run: ;\
java -jar eclass.jar

clean: ;\
rm -rf bin/application/*

copy_dependencies: ;\
cd bin;\
cp ../src/application/*.fxml application;\
cp ../src/application/*.png  application;\
cp ../src/application/*.gif  application;\
