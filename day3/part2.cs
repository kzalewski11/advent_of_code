using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace Advent_of_Code
{
    class Day4
    {
        static void Main()
        {
            List<string> entries = new List<string>();
						uint treeMult = 0;

            //Let's populate the list from file
            foreach (string line in File.ReadLines(@".\input.txt"))
            {
                entries.Add(line);                
            }

            int x = 0, trees = 0;
						int rightmoves = 1, downmoves = 1;
            for(int y=downmoves; y < entries.Count; y += downmoves)
            {
                if ((x += rightmoves) > (entries[y].Length-1))
                    x -= entries[y].Length;

                if(entries[y][x] == '#')
                    trees++;                
            }
						treeMult = (uint)trees;

						x = 0;
						trees = 0;
						rightmoves = 3;
						downmoves = 1;
						for(int y=downmoves; y < entries.Count; y += downmoves)
						{
								if ((x += rightmoves) > (entries[y].Length-1))
										x -= entries[y].Length;

								if(entries[y][x] == '#')
										trees++;                
						}
						treeMult *= (uint)trees;

						x = 0;
						trees = 0;
						rightmoves = 5;
						downmoves = 1;
						for(int y=downmoves; y < entries.Count; y += downmoves)
						{
								if ((x += rightmoves) > (entries[y].Length-1))
										x -= entries[y].Length;

								if(entries[y][x] == '#')
										trees++;                
						}
						treeMult *= (uint)trees;

						x = 0;
						trees = 0;
						rightmoves = 7;
						downmoves = 1;
						for(int y=downmoves; y < entries.Count; y += downmoves)
						{
								if ((x += rightmoves) > (entries[y].Length-1))
										x -= entries[y].Length;

								if(entries[y][x] == '#')
										trees++;                
						}
						treeMult *= (uint)trees;

						x = 0;
						trees = 0;
						rightmoves = 1;
						downmoves = 2;
						for(int y=downmoves; y < entries.Count; y += downmoves)
						{
								if ((x += rightmoves) > (entries[y].Length-1))
										x -= entries[y].Length;

								if(entries[y][x] == '#')
										trees++;                
						}
						treeMult *= (uint)trees;
            Console.Write(treeMult + " is your answer you dumb bitch");
            Console.ReadKey();
        }
    }
}
