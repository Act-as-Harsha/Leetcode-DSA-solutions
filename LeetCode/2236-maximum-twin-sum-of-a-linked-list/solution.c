/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head) {
    int ans = 0;
    struct ListNode* newList = NULL;
    struct ListNode* current = head;
    struct ListNode* currHalf = head;
    
    while (currHalf && currHalf->next) {
        currHalf = currHalf->next->next;
        struct ListNode* temp = current->next;
        current->next = newList;
        newList = current;
        current = temp;
    }

    while (current) {
        ans = fmax(ans, (current->val + newList->val));
        current = current->next;
        newList = newList->next;
    }
    
    return ans;
}
