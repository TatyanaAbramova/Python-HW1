# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

A = [int(input('Введите координату "x" точки A:\n')), int(input('Введите координату "y" точки A:\n'))]
B = [int(input('Введите координатy "x" точки B:\n')), int(input('Введите координатy "y" точки B:\n'))]
AB = (((A[0]-B[0])**2) + ((A[1]-B[1])**2)) **0.5
print ('AB = ', round(AB, 2))
