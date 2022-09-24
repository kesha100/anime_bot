# from time import sleep
# import asyncio
#
#
# async def download_photo(photo_count):
#     while True:
#         await asyncio.sleep(1)
#         photo_count += 1
#         print(f'Photo {photo_count} ...')
#
#
# async def download_video(video_count):
#     while True:
#         await asyncio.sleep(5)
#         video_count += 1
#         print(f'Video {video_count} ...')
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count),
#         download_video(video_count)
#     ]
#     await asyncio.gather(*task_list)
#
#
# # asyncio.run(main())
#
# async def download_photo2(current_photo):
#     await asyncio.sleep(1)
#     print(f'Photo {current_photo} ...')
#
#
# async def main2():
#     task_list = []
#     count = int(input('Enter amount of photo: '))
#     current_photo = 0
#     while current_photo < count:
#         current_photo += 1
#         task = asyncio.create_task(download_photo2(current_photo))
#         task_list.append(task)
#     await asyncio.gather(*task_list)
#     print('Done')
#
# asyncio.run(main2())
#
# #
# # if __name__ == '__main__':
# #     main2()