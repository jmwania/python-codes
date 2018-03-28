# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
def count_smileys(smileys):
    smiley_counter = 0
    valid_smileys = [':)',':-)',':~)',';)',';-)',';~)',':D',':-D',':~D',';D',';-D',';~D']
    for smiley in smileys:
        if smiley in valid_smileys:
            smiley_counter += 1
    return smiley_counter

print (count_smileys([';]', ':[', ';*', ':$', ';-D']))