Name:		texlive-modref
Version:	15878
Release:	1
Summary:	Customisation of cross-references in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains macros which allow authors to easily
customise how cross-references appear in their document, both
in general (across all cross-references) and for particular
types of references (identified by a prefix in the reference
label), in a very generic manner.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/modref/modref.sty
%doc %{_texmfdistdir}/doc/latex/modref/README
%doc %{_texmfdistdir}/doc/latex/modref/modref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/modref/modref.drv
%doc %{_texmfdistdir}/source/latex/modref/modref.dtx
%doc %{_texmfdistdir}/source/latex/modref/modref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
