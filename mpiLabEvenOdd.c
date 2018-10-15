#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]){
	MPI_Init(NULL, NULL);
	int number, value;
	int world_size;
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);
	int world_rank;
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

	if (world_size != 3){
		fprintf(stderr, "This application must contain exactly 3 processes %s\n", argv[0]);
		MPI_Abort(MPI_COMM_WORLD, 1);
	}

	if (world_rank == 0){
		printf("Enter a number\n");
		scanf("%d", &number);
		MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
	}
	else if (world_rank == 1){
		MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		if (number % 2 == 0){
			value = 1;
		}
		else{
			value = 0;
		}
		MPI_Send(&value, 1, MPI_INT, 2, 1, MPI_COMM_WORLD);
	}
	else if (world_rank == 2){
		MPI_Recv(&value, 1, MPI_INT, 1, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		if (value == 1)
			printf("Even\n");
		else
			printf("Odd\n");
	}
	MPI_Finalize();
}