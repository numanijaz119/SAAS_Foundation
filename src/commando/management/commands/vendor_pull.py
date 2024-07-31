import helper
from typing import Any
from django.conf import settings
from django.core.management.base import BaseCommand

STATICFILES_VENDOR_DIR = settings.STATICFILES_VENDOR_DIR

VENDER_STATICFILES = {
    'flowbite.min.css':'https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.css',
    'flowbite.min.js':'https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.js',
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")
        completed_url  = []
        for name, url in VENDER_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helper.download_file(url, out_path)
            if dl_success:
                completed_url.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}"))
            
        if set(completed_url) == set(VENDER_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS("Successfully updated Vendor Static files"))
        else: 
            self.stdout.write(self.style.ERROR("Failed to download Vendor Static files"))