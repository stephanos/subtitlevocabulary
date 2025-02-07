const Nav = ({ analysis, word, onClick }) =>
    <nav className='navigation'>
        <section className='container'>
            <span className='navigation-title'>
                <h1 className='title'>
                    { analysis && word && word.token
                        ? <div className='media' onClick={onClick}>
                            <span className="arrow left">&gt;</span>
                            <span className="name">{ analysis.media.title }</span>
                        </div>
                        : <a className='generic' href="/">
                            subvoc
                        </a>
                    }
                </h1>
            </span>
        </section>
    </nav>;


export { Nav };