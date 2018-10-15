#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]){
	MPI_Init(NULL, NULL);

	int world_rank, data, i;
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
	int world_size;
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);

	if (world_rank == 0)
		data = 5;

	MPI_Bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);

	for (i = 1; i < 3; i++){
		printf("world_rank %d, data %d\n", world_rank, data);
	}
	MPI_Finalize();
}