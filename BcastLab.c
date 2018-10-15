#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <string.h>

int main(int argc, char* argv[]){
	char arr[6];
	MPI_Init(NULL, NULL);

	int world_size;
	MPI_Comm_size(MPI_COMM_WORLD, &world_size);

	int world_rank;
	MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

	if (world_rank == 0){
		strcpy(arr, "hello");
	}

	MPI_Bcast(arr, 5, MPI_UNSIGNED_CHAR, 0, MPI_COMM_WORLD);

	printf("[%d]: After Bcast, array is %c%c%c%c%c\n", world_rank, arr[0], arr[1], arr[2], arr[3], arr[4]);
	MPI_Finalize();
	return 0;

}