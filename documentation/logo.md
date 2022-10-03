# Logo

Tässä dokumentissa on koostettuna projektissa käytetyn logo-kielen sääntöjä.

## Muuttujat

Muuttuja määritetään avainsanalla make tai tee, ja antamalla " ennen muuttujan nimeä. Muuttujan arvo annetaan muuttujan nimeämisen jälkeen. Esimerkiksi muuttujalle x annetaan arvo 42
`make "x 42`

Muuttujaan viitataan kaksoispisteellä. Esimerkiksi muuttujan x arvo tulostetaan avainsanalla show, print, sano tai tulosta
`show :x`

## Funktiot

Funktioilla on oma näkyvyysalue, eikä funktion ulkopuolella määriteltyjä muuttujia pysty käyttämään funktion sisällä, ellei niitä anna parametreina. Luodaan esimerkiksi funktio foo, joka tulostaa saamansa parametrin n arvon

```
TO foo :n
  show :n
END
```

Funktiota voidaan kutsua muuttujalla x
```
MAKE "x 42
foo :x
```

Funktiota **ei voida** kuitenkaan määritellä ja kutsua globaalilla muuttujalla, sillä funktion ulkopuolella määritetyt muuttujat eivät näy funktion sisälle.
```
TO foo 
  show :x
END

MAKE "x 42
foo
ERR
```

## Ehtolauseet

Alla oleva koodi määrittää muuttujan x arvoksi luvun 42. Jos arvo on alle 100, tulostetaan muuttujan x arvo. 
```
make "x 42
if :x < 100 {
    print :x
}
```

Ehtolauseissa voidaan siis viitata ehtolauseen ulkopuolella oleviin muuttujiin. Ehtolauseilla on kuitenkin oma näkyvyysalue, eli ehtolauseen sisällä voidaan määrittää muuttujia, jotka eivät näy ehtolauseen ulkopuolelle. Seuraava koodi kaatuu virheeseen, sillä muuttujaan y viitataan ehtolauseen ulkopuolella.
```
make "x 42
if :x < 100 {
    make "y 123
}
show :y
ERR
```