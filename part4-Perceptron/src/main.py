from perceptron import Perceptron
from nn import Nn

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'


def main():
    """
    Implement the perceptron algorithm in the Perceptron class. After that you can try out the
    values of different number pairs by changing the values of the 'target_char' and
    'opposite_char' variables.
    """
    perc = Perceptron(IMGS_FILE, CHARS_FILE)
    #perc.train('3', '5', 100)
    #print(perc.test('3', '5'))
    #perc.save_weights('weights.bmp')

    nn = Nn(perc.data[:5000])
    print("Testing nearest neighbor classifier:")
    count = 0
    for x in perc.data[5000:]:
        label = str(nn.classify(x["vector"]))
        if x["char"] == label:
            count += 1
        print(x["char"] + " classified as: " + label)
    print("Classified with " + str(count/1000) + " accuracy") #0.924


if __name__ == '__main__':
    main()
