from build_deck import *

if __name__ == "__main__":
    
    deck = [
        {
            "id":"1f1255a4-686a-66b0-616b-9bf03ff38a8e",
            "collectionId":"1f110bee-01f3-6bd0-6d90-6b54d4f111f7",
            "equipmentId":"1f09e0bd-e101-6470-ec79-2c9d42f67a39_ee9a8b9755c8e1670ec0be4da458e65e",
            
            },
        {
            "id":"1f119fde-d4f3-6f10-fe05-a9a773d83f22",
            "collectionId":"1f110bee-01f3-6bd0-6d90-6b54d4f111f7",
            },
        {
            "id":"1f11231d-360c-6cf0-d690-88eefa58045d",
            "collectionId":"1f003090-2aee-6250-109f-d0272367a2ef",
            },
        {
            "id":"1f11d7b8-4fc5-6bb0-2bbb-741050c34ed3",
            "collectionId":"1f084e09-fee2-6310-25d6-35154b276a8c",
            },
        {
            "id":"1f120fee-8246-6f80-2a31-95d4ac29c0d6",
            "collectionId":"1f07783a-3bb0-6810-c213-f5f53af5f2c8",
            }
        ]
    

    print(build_deck_division(deck))
    print(build_deck_commun_cup(deck))
    print(build_deck_limited_cup(deck))
    print(build_deck_rare_cup(deck))
    print(build_deck_epic_cup(deck))
    print(build_deck_legendary_cup(deck))