class Room:
    def __init__(self, room_number, price, is_booked=False):
        self.room_number = room_number
        self.price = price
        self.is_booked = is_booked
class Hotel:
    def __init__(self):
        self.rooms = []
    def add_room(self, room):
        self.rooms.append(room)
        print(f"Đã thêm phòng {room.price} - {room.room_number}")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_booked:
                    room.is_booked = True
                    print(f"Phòng {room_number} đã được đặt")
                    return
                else:
                    print(f"Phòng {room_number} đã có người đặt!")
                    return
        print(f"Không tìm thấy phòng {room_number}!")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_booked:
                    room.is_booked = False
                    print(f"Phòng {room_number} đã được trả")
                    return
                else:
                    print(f"Phòng {room_number} đang không có ai ở")
                    return
        print(f"Không tìm thấy phòng {room_number}!")

ks = Hotel()
room1 = Room(201, 500000)
room2 = Room(202, 500000)
room3 = Room(203, 500000)
ks.add_room(room1)
ks.add_room(room2)
ks.add_room(room3)
ks.book_room(201)
ks.check_out(201)