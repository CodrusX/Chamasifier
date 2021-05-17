a=118
for f in *.jpeg; do
    mv -- "$f" "$a.jpeg"
    ((a = a + 1))
done
