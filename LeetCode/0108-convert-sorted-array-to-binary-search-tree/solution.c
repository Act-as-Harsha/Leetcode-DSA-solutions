struct TreeNode* createNode(int data) {
    struct TreeNode* newnode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    if (!newnode) {
        return NULL; 
    }
    newnode->val = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}

struct TreeNode* sortedArrayToBSTRecur(int nums[], int start, int end) {
    if (start > end) return NULL;

    
    int mid = start + (end - start) / 2;

  
    struct TreeNode* root = createNode(nums[mid]);

    root->left = sortedArrayToBSTRecur(nums, start, mid - 1);

    root->right = sortedArrayToBSTRecur(nums, mid + 1, end);

    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return sortedArrayToBSTRecur(nums, 0, numsSize - 1);
}
