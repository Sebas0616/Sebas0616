package Logica;


public class GuitarraA implements IGuitarra{

    @Override
    public void tocar() {
        System.out.println("Tocando guitarra acustica");
    }

    @Override
    public void parar() {
        System.out.println("Dejando de tocar guitarra acustica");
    }
    
}
