from os import getenv
import sys
import csv
from microsofttranslator import Translator





def read_word_list():
    with open('625-words-fluent-forever.csv', 'rb') as csvfile:
        wordreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        en_word_list = []
        for row in wordreader:
            en_word_list.append(row[0])
        return en_word_list


def get_translated_text(en_word_list, target_language, client_id, api_key):
    translator = Translator(client_id, api_key)
    result = translator.translate_array(en_word_list, target_language)
    word_list = [i['TranslatedText'] for i in result]
    word_list.insert(0, target_language)
    return word_list

def write_result(to_write_matrix):
    with open('625-words-fluent-forever-output.csv', 'wb') as csvfile:
        word_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in to_write_matrix:
            row=[s.encode('utf-8') for s in row] # encode so CSV gets written correctly
            word_writer.writerow(row)

def run():
    """Main function to query Microsoft Translator API and translate words

    :return:
    """


    try:
        client_id = getenv('MS_TRANSLATOR_CLIENT_ID', None)
        api_key = getenv('MS_TRANSLATOR_API_KEY', None)

        if not api_key:
            client_id = str(raw_input('Microsoft Translator Client ID: '))
            api_key = str(raw_input('Microsoft Translator API Key: '))
        if client_id and api_key:

            translator = Translator(client_id, api_key)
            en_word_list = read_word_list()
            result_matrix = []

            for lang in translator.get_languages(): #

                result = get_translated_text(en_word_list, lang, client_id, api_key)
                result_matrix.append(result)

            # Transpose the matrix for csv writer
            to_write_matrix = [list(i) for i in zip(*result_matrix)]
            write_result(to_write_matrix)
    except:
        sys.exit(2)


if __name__ == '__main__':
    run()
