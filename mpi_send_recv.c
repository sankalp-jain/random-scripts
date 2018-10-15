#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]){
	MPI_Init(NULL, NULL);

	int world_size;
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);

	int world_rank;
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

	if (world_size < 2){
		fprintf(stderr, "World size should be greater than 1 for %s\n", argv[0]);
		MPI_Abort(MPI_COMM_WORLD, 1);
	}

	int number;
	if (world_rank == 0){
		printf("%d\n", world_rank);
		number = -1;
		MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
	}
	else if (world_rank == 1){
		MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
		printf("Process 1 received %d from Process 0\n", number);
	}

	MPI_Finalize();
}