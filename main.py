from functions import post_to_fb_page, get_featured_recipie

if __name__ == '__main__':
    is_posted = False
    title, image_url = get_featured_recipie()
    is_posted = post_to_fb_page(msg=title, image_url=image_url)
    if is_posted:
        print('Successfully Posted')
