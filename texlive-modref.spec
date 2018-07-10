# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/modref
# catalog-date 2009-02-09 16:57:43 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-modref
Version:	1.0
Release:	11
Summary:	Customisation of cross-references in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754094
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719055
- texlive-modref
- texlive-modref
- texlive-modref
- texlive-modref

