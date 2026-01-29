print("\n*** Cafézinho ***\n")


agua = 0.310   # referência para água
acucar = 1.5   # referência para "scoop" de açúcar
cafe = 3       # referência colheres de pó


ml = float(input("Quantos ml de água pretende utilizar para o cafézinho? "))

colheres_cafe = cafe * (ml / agua)
scoops_acucar = acucar * (ml / agua)


print(f"Para {ml:.3f} ml de cafézinho, você deve usar:")
print(f"- {colheres_cafe:.2f} colheres de pó de café")
print(f"- {scoops_acucar:.2f} scoops de açúcar")

art = r"""
         (  )   (   )  )
          ) (   )  (  (
          ( )  (    ) )
          _____________
         <_____________> ___
         |             |/ _ \
         |               | | |
         |               |_| |
      ___|             |\___/
     /    \___________/    \
     \______________________/
"""
print(art)