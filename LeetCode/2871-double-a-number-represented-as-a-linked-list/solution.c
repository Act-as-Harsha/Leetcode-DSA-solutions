
struct ListNode* reverse(struct ListNode* head) {
    struct ListNode *prev = NULL, *curr = head;
    while (curr) {
        struct ListNode* nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}
struct ListNode* new_ListNode(int data) {
    struct ListNode* newNode =
        (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->next = NULL;
    newNode->val = data;
    return newNode;
}
struct ListNode* doubleIt(struct ListNode* head) {
    head = reverse(head);
    int carry = 0;
    struct ListNode* temp = head;
    int product = (temp->val) << 1;
    if (product > 9) {
        carry = product / 10;
        product %= 10;
    }
    struct ListNode* dummyHead = new_ListNode(product);
    struct ListNode *prev = dummyHead, *dummy_head = dummyHead;
    temp = temp->next;
    while (temp) {
        product = (temp->val) << 1;
        product += carry;
        carry = product / 10;
        if (product > 9) {
            product %= 10;
        }
        struct ListNode* newNode = new_ListNode(product);
        prev->next = newNode;
        prev = newNode;
        temp = temp->next;
    }
    if (carry) {
        struct ListNode* newNode = new_ListNode(carry);
        prev->next = newNode;
        prev = newNode;
    }
    return reverse(dummy_head);
}
