# from kamata3 import obracun_kredita
import kamata3

# iznos = obracun_kredita([1000,2000,3000],0.08,10)
if __name__ == '__main__':
    iznos = kamata3.obracun_kredita([1000,2000,3000],0.08,10)
    print(iznos)
    print('kamata4 name: ',__name__)