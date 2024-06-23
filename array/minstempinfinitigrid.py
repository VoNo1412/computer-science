def minStepInfinitiGrid(A = [], B = []):
    totalSteps = 0;
        
    for i in range(len(A) - 1):
        dx = A[i + 1] - A[i];
        dy = B[i + 1] - B[i];

        totalSteps += max(dx, dy);

    return totalSteps


print(minStepInfinitiGrid([0, 1, 1], [0, 1, 2]))