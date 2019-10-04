package Logica;


public class GuitarraE implements IGuitarra, IGuitarraE{

    
    @Override
    public void conectar() {
        System.out.println("Conectando amplificardor a la guitarra eléctrica");
    }
    
    @Override
    public void tocar() {
        conectar();
        System.out.println("Tocando guitarra eléctrica");
    }
    
    @Override
    public void parar() {
        System.out.println("Dejando de tocar guitarra eléctrica");
        desconectar();
    }
    
    @Override
    public void desconectar() {
        System.out.println("Desconectando amplificardor de la guitarra eléctrica");
    }  
}
