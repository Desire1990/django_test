from django.contrib import admin

from .models import Booking, Contact, Artist, Album


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
	list_filter = ['created_at', 'contacted']

class BookingInline(admin.TabularInline):
	model = Booking
	fieldsets=[(None, {'fields': ['album', 'contacted']})] # list columns]       
	extra = 0
	verbose_name = 'Reservation'
	verbose_name_plural = 'Reservations'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,] # list of bookings made by a contact

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	search_fields = ['reference', 'title']

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through # the query goes through an intermediate table.
    extra = 1

    verbose_name = 'Disque'
    verbose_name_plural = 'Disques'

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]