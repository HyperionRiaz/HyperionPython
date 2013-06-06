import java.io.*;	
import java.util.*;
	
	public class answer 
	{ 

		public static void main(String[] args)
		{
			HashMap<String, int[]> ips = new HashMap<String, int[]>();

			if (args.length == 0)
			{
				System.out.println("Please give arguments of files you want to join");
			}
			else
			{
			
				for (int i =0; i < args.length; i++)
				{
				
					BufferedReader br = null;
					
					try
					{
						String line = "";
						br = new BufferedReader(new FileReader(args[i]));
					
						while ( (line = br.readLine()) != null) {
						
							System.out.println(line);
							if (line.indexOf(":") == -1) //Malformed line
							{
								continue; 
							}
							else
							{
								String IP = line.substring(0,line.indexOf(":"));
								String number = line.substring(line.indexOf(":")+2);
								String[] numbers = number.split(",");
								int[] tmp = new int[numbers.length];
								
								for (int o = 0; o < numbers.length; o++)
								{
									tmp[o] = Integer.parseInt(numbers[o]);
	
							
								}
				
								 ips.put(IP, tmp);
								//
							}
							
							
							//Sytem.out.println(ips.get("a")+"");
						}
						
						
					
					}
					catch (IOException e)
					{
						System.out.println("Oops");
						e.printStackTrace();
						
					}
				}
				
				
				
				
				
				
			}

		}


	}