%define _disable_ld_no_undefined 1
%define _disable_lto 1

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Summary:	Simple console audio player
Name:		moc
Version:	2.5.2
Release:	3
Epoch:		1
License:	GPLv2+
Group:		Sound
URL:		https://moc.daper.net/
Source0:	http://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	libmpc-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	faac-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	db-devel
BuildRequires:	libtool-devel
BuildRequires:	autogen
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(popt)
BuildRequires:	locales-extra-charsets

%description
MOC is a console audio player with ncurses interface
Features:
  * Supports aac ffmpeg flac modplug mp3 musepack sndfile speex vorbis wavpack
  * Play files from directory changing automatically to the next one
    without any playlist.
  * Supports id3tag, VBR and Xing header for MP3.
  * Simple mixer.
  * Fast switching to your music directory.
  * Playlists (without read/write to a file).
  * Shuffle and repeat.
  * Changing process priority to higher value.
  * Playing in separate thread.

%prep
%setup -q

%build
export CFLAGS="%{optflags} `pkg-config --cflags ncursesw`"

# --without-ffmpeg because ffmpeg 5.x isn't supported
%configure \
	--without-ffmpeg
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/share/doc/
rm -rf %{buildroot}/%{_libdir}/*/*/*la

%files
%doc COPYING AUTHORS NEWS README TODO
%doc config.example keymap.example
%{_bindir}/mocp
%{_mandir}/*/*
%{_libdir}/%{name}
%{_datadir}/%{name}
