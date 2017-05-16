package WorkSpace;

public class mainSpace {
	public static void main(String args[]){		
		int poly_deg = 5; // you can only put 6 and 7.
		int seq_length = mSeqlength.seq_length(poly_deg);
		System.out.println("The Sequences length is: "+seq_length);
		
		// Initialising the shift registers		
		int [] init_state = new int[poly_deg];		
		init_state[poly_deg-1] = 1;
		
		// Generating the two m-sequences 
		int [] seqA = mSeqGenA.PNseq(poly_deg, seq_length, init_state);
		int [] seqB = mSeqGenB.PNseq(poly_deg, seq_length, init_state);
		System.out.println("");

		// Generating the Gold Code
		int [] gold = goldCodeGen.gold(seq_length, seqA, seqB);
		
	}
}

// calculating the sequences length
public class mSeqlength {
	public static int seq_length (int deg){
		int length = (int)(Math.pow(2,deg) - 1);
		System.out.println("");
		return length;
		}
	}

// generating the first m-sequence (make sure to XOR the right taps)
public class mSeqGenA {
	public static int []PNseq (int poly_deg, int seq_length, int
[]taps_seed){
		
		int i,j;
		int xor1, xor2;
		int [] PNseq = new int[seq_length];
		int [] temp = new int[poly_deg];
		
		temp = taps_seed;
		
		System.out.println("the first m-sequence is: ");
		
		if (seq_length<32){
			for (i=0; i<seq_length; i++){	
			
			xor2 = taps_seed[3] ^ taps_seed[poly_deg-1];
			xor2 = xor2 ^ taps_seed[2];
			xor1 = xor2 ^ taps_seed[1];
			
			//shifting the taps
			for (j=(poly_deg-1); j>0; j--){
					temp[j]= taps_seed[j-1];
				}
				j=0;				
				temp[j] = xor1;
				
			PNseq[i] = taps_seed[poly_deg-1];
			taps_seed = temp;
				}
			
			for (i=seq_length; i>0; i--){
				System.out.print(PNseq[i-1]);}
				System.out.println("");
		}
		else if(seq_length>32){
			if (seq_length<64){
				for (i=0; i<seq_length; i++){	
					
					xor2 = taps_seed[4] ^ taps_seed[poly_deg-1];
					xor2 = xor2 ^ taps_seed[1];
					xor1 = xor2 ^ taps_seed[0];
					
					//shifting the sequence
					for (j=(poly_deg-1); j>0; j--){
							temp[j]= taps_seed[j-1];
						}
						j=0;				
						temp[j] = xor1;
						
					PNseq[i] = taps_seed[poly_deg-1];
					taps_seed = temp;
						}
				
						for (i=0; i<seq_length; i++){
							System.out.print(PNseq[i]);}
							System.out.println("");
			}
			else if (seq_length>64){
				for (i=0; i<seq_length; i++){	
					
					xor2 = taps_seed[5] ^ taps_seed[poly_deg-1];
					xor2 = xor2 ^ taps_seed[4];
					xor1 = xor2 ^ taps_seed[3];
					
					//shifting the sequence
					for (j=(poly_deg-1); j>0; j--){
							temp[j]= taps_seed[j-1];
						}
						j=0;				
						temp[j] = xor1;
						
					PNseq[i] = taps_seed[poly_deg-1];
					taps_seed = temp;
						}
					
						for (i=0; i<seq_length; i++){
							System.out.print(PNseq[i]);}
							System.out.println("");
			}
		}
	return PNseq;
	}

}

// generating the second m-sequence (make sure to XOR the right taps)
public class mSeqGenB {
	public static int [] PNseq (int poly_deg, int seq_length, int
[]taps_seed){
		
		int i, j;
		int xor1;
		int [] PNseq = new int[seq_length];
		int [] temp = new int[poly_deg];
		temp = taps_seed;
		
		System.out.println("the second m-sequence is: ");
		
		if (seq_length<=32){
			for (i=0; i<seq_length; i++){	
		
				xor1 = taps_seed[2] ^ taps_seed[poly_deg-1];
				
				//shifting the taps
				for (j=(poly_deg-1); j>0; j--){
						temp[j]= taps_seed[j-1];
					}
					j=0;				
					temp[j] = xor1;
					
				PNseq[i] = taps_seed[poly_deg-1];
				taps_seed = temp;
					}
				
			for (i=seq_length; i>0; i--){
				System.out.print(PNseq[i-1]);}
				System.out.println("");
		}
		else if (seq_length>31){
			if (seq_length<=64){
				for (i=0; i<seq_length; i++){	
					
					xor1 = taps_seed[0] ^ taps_seed[poly_deg-1];
					
					for (j=(poly_deg-1); j>0; j--){
							temp[j]= taps_seed[j-1];
						}
						j=0;				
						temp[j] = xor1;
						
					PNseq[i] = taps_seed[poly_deg-1];
					taps_seed = temp;
						}
					
				for (i=0; i<seq_length; i++){
					System.out.print(PNseq[i]);}
					System.out.println("");
			}
			else if (seq_length>64){
				for (i=0; i<seq_length; i++){	
					
					xor1 = taps_seed[3] ^ taps_seed[poly_deg-1];
					
					for (j=(poly_deg-1); j>0; j--){
							temp[j]= taps_seed[j-1];
						}
						j=0;				
						temp[j] = xor1;
						
					PNseq[i] = taps_seed[poly_deg-1];
					taps_seed = temp;
						}
					
				for (i=0; i<seq_length; i++){
					System.out.print(PNseq[i]);}
					System.out.println("");
			}

		}
			
	return PNseq; 
	}
}

// where gold codes are generated
public class goldCodeGen 
{
	public static int [] gold (int seq_length, int []seqA, int []seqB)
	{
		int i, j, d;
		int []gold_code = new int[seq_length];
				
		for (d=0; d<seq_length; d++){
			int []temp = new int[seq_length];
			
			// generating the gold code
			for (i=0; i<seq_length; i++){
				gold_code[i] = seqA[i] ^ seqB[i];} 
				// showing the gold code
				for (i=seq_length; i>0; i--){
					System.out.print(gold_code[i-1]);
					} 
					
			//checking if the gold sequence is balanced
			int zeros=0, ones=0;
			for (i=0; i<seq_length; i++){
				if (gold_code[i]==0){
					zeros= zeros+1;}
				else {ones= ones+1;}
				}			
			if ((zeros==ones) || (zeros==(ones-1))) 
			{System.out.println(" 'Balanced'");}
				else {
					System.out.println(" 'NOT balanced'");
					}
			
			//shifting the second m-sequence
			for (j=(seq_length-1); j>0; j--){
				temp[j] = seqB[j-1];
				}
				j=0;
				temp[j] = seqB[(seq_length-1)];
			
			seqB = temp;
			}
		return gold_code;
	}
}
