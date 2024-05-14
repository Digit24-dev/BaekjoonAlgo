#include <stdio.h>

typedef struct Node{
    int val;
    Node *left;
    Node *right;
} Node;

int count(Node *root)
{
    if (root == NULL) return 0;
    
    int ret = 1;
    
    if (root->left != NULL)
        ret += count(root->left);
    
    if (root->right != NULL)
        ret += count(root->right);
    
    return ret;
}

int count2(Node *root)
{
    if (root == NULL)
        return 0;

    return count2(root->left) + count2(root->right) + 1;
}