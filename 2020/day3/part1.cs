using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace Advent_of_Code
{
    class Day3
    {
        static void Main()
        {
            List<string> entries = new List<string>();

            //Let's populate the list from file
            foreach (string line in File.ReadLines(@".\input.txt"))
            {
                entries.Add(line);                
            }

            int x = 0, trees = 0;

            for(int y=1; y < entries.Count; y++)
            {
                if ((x += 3) > (entries[y].Length-1)) 
                    x -= entries[y].Length;


                if(entries[y][x] == '#')
                    trees++;                
            }

            //foreach(string entry in entries)
            //  Console.Write(entry);

            Console.Write(trees + " were hit you dumb bitch");

            Console.ReadKey();


        }
    }
}
