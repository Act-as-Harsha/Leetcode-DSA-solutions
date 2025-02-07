
int getLength(struct ListNode* head) {
    int cnt = 0;
    struct ListNode* temp = head;
    while (temp) {
        cnt++;
        temp = temp->next;
    }
    return cnt;
}

struct ListNode* swapNodes(struct ListNode* head, int k) {
    if (head == NULL || head->next == NULL)
        return head;
    int len = getLength(head);
    struct ListNode *ptr1 = head, *ptr2 = head;
    for (int i = 1; i < k; ++i)
        ptr1 = ptr1->next;

    for (int i = 1; i < len - k + 1; ++i)
        ptr2 = ptr2->next;

    int temp = ptr1->val;
    ptr1->val = ptr2->val;
    ptr2->val = temp;
    return head;
}
