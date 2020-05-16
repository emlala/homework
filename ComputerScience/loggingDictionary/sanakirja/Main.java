package sanakirja;

import java.io.FileNotFoundException;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        // for testing the dictionary

        MuistavaSanakirja sanakirja = new MuistavaSanakirja("loggingDictionary/sanat.txt");
        boolean onnistui = sanakirja.lataa();

        if (onnistui) {
            System.out.println("sanakirjan lataaminen onnistui");
        }

        System.out.println(sanakirja.kaanna("apina"));
        System.out.println(sanakirja.kaanna("ohjelmointi"));
        System.out.println(sanakirja.kaanna("alla oleva"));
        sanakirja.lisaa("koira", "dog");
        sanakirja.lisaa("kirjasto", "library");

        sanakirja.tallenna();
    }
}